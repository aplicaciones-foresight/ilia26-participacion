import openpyxl

PAISES = ["AR","BO","BR","CL","CO","CR","CU","DO","EC","GT","HN","JM","MX","PA","PE","PY","SV","UY","VE"]

def load_casos():
    wb = openpyxl.load_workbook("/mnt/user-data/uploads/BBDD_IA_para_Participación_-_Entrega.xlsx", data_only=True)
    ws = wb["BBDD Casos"]
    casos=[]
    for row in ws.iter_rows(min_row=2, max_row=ws.max_row, values_only=True):
        if row[0] is None or row[1] is None: continue
        if str(row[0]).strip()=="" or str(row[1]).strip()=="": continue
        casos.append({
            "pais": str(row[0]).strip(), "caso": str(row[1]).strip(),
            "ano": row[2], "activo": str(row[3]).strip() if row[3] else "",
            "tipo_org": str(row[6]).strip() if row[6] else "",
            "tipos_ia": str(row[9]).strip() if row[9] else "",
            "tipo_proceso": str(row[11]).strip() if row[11] else "",
            "etapa": str(row[12]).strip() if row[12] else "",
            "desarrollador": str(row[14]).strip() if row[14] else "",
            "origen": str(row[15]).strip() if row[15] else "",
            "continuidad": str(row[17]).strip() if row[17] else "",
        })
    return casos

def split_clean(s):
    return [x.strip() for x in s.replace(";",",").split(",") if x.strip()]
PROC_MAP={"participación digital":"Participación digital","participacion digital":"Participación digital",
    "governanza colaborativa":"Governanza","governanza participativa":"Governanza",
    "mini públicos":"Mini públicos","mini publicos":"Mini públicos",
    "referendos e iniciativas populares":"Referendos","referendos":"Referendos",
    "presupuestos participativos":"Presupuestos participativos"}
def norm_proc(p): return PROC_MAP.get(p.lower().strip())
def norm_etapa(e):
    e=e.lower()
    if "planif" in e: return "Planificación"
    if "implement" in e: return "Implementación"
    if "análisis" in e or "analisis" in e: return "Análisis"
    if "traducción" in e or "traduccion" in e: return "Traducción Política"
    return None
def norm_org(o):
    o=o.lower()
    if "mixto" in o: return "Mixto"
    if "público" in o or "publico" in o: return "Público"
    if "privado" in o: return "Privado"
    return None
DEV_MAP={"industria":"Empresa","academia":"Universidad","gobierno":"Gobierno","sociedad civil":"Sociedad Civil"}
def norm_dev(d): return DEV_MAP.get(d.lower().strip())

def raw_counts(casos_list):
    """Conteos crudos por país."""
    out={}
    for p in PAISES:
        cp=[c for c in casos_list if c["pais"]==p]
        tipos=set();etapas=set();cont=set();orgs=set()
        dev_nac=set();dev_int=set();sistemas=set()
        for c in cp:
            for x in split_clean(c["tipo_proceso"]):
                m=norm_proc(x);  tipos.add(m) if m else None
            for x in split_clean(c["etapa"]):
                m=norm_etapa(x); etapas.add(m) if m else None
            cc=c["continuidad"].lower()
            if "único" in cc or "unico" in cc: cont.add("UU")
            if "plataforma" in cc: cont.add("PL")
            m=norm_org(c["tipo_org"]); orgs.add(m) if m else None
            devs=[norm_dev(x) for x in split_clean(c["desarrollador"])]
            devs=[d for d in devs if d]
            origs=[o.lower() for o in split_clean(c["origen"])]
            has_nac=any("nacional" in o for o in origs)
            has_int=any("internacional" in o for o in origs)
            # internacional primero (porque "internacional" contiene "nacional")
            has_nac=any(o=="nacional" for o in origs)
            for d in devs:
                if has_nac: dev_nac.add(d)
                if has_int: dev_int.add(d)
            for s in split_clean(c["tipos_ia"]):
                sistemas.add(s.lower())
        out[p]={"tipos":len(tipos),"etapas":len(etapas),"cont":len(cont),"orgs":len(orgs),
                "dev_nac":len(dev_nac),"dev_int":len(dev_int),"sistemas":len(sistemas),"n":len(cp)}
    return out

def compute_full(casos_list, estado_func=None, use_5var=False):
    """Calcula sub1, sub2, indicador. estado_func(caso)->peso si use_5var."""
    rc=raw_counts(casos_list)
    # Sub1 (max absoluto)
    sub1={}
    for p in PAISES:
        d=rc[p]
        if d["n"]==0: 
            sub1[p]={"v":0,"tipos":0,"etapas":0,"cont":0,"pp":0,"estado":0}; continue
        v_tipos=d["tipos"]/5*100; v_etapas=d["etapas"]/4*100
        v_cont=d["cont"]/2*100; v_pp=d["orgs"]/3*100
        if use_5var:
            cp=[c for c in casos_list if c["pais"]==p]
            pesos=[estado_func(c) for c in cp]
            v_estado=sum(pesos)/len(pesos)*100
            v=(v_tipos+v_etapas+v_cont+v_pp+v_estado)/5
            sub1[p]={"v":round(v),"tipos":round(v_tipos),"etapas":round(v_etapas),
                     "cont":round(v_cont),"pp":round(v_pp),"estado":round(v_estado)}
        else:
            v=(v_tipos+v_etapas+v_cont+v_pp)/4
            sub1[p]={"v":round(v),"tipos":round(v_tipos),"etapas":round(v_etapas),
                     "cont":round(v_cont),"pp":round(v_pp),"estado":None}
    # Sub2 (max relativo): dividir por max observado
    max_nac=max((rc[p]["dev_nac"] for p in PAISES), default=0) or 1
    max_int=max((rc[p]["dev_int"] for p in PAISES), default=0) or 1
    max_sis=max((rc[p]["sistemas"] for p in PAISES), default=0) or 1
    sub2={}
    for p in PAISES:
        d=rc[p]
        if d["n"]==0:
            sub2[p]={"v":0,"dev":0,"sis":0}; continue
        nac=d["dev_nac"]/max_nac*100
        intl=d["dev_int"]/max_int*100
        dev=(nac+intl)/2
        sis=d["sistemas"]/max_sis*100
        v=(dev+sis)/2
        sub2[p]={"v":round(v),"dev":round(dev),"sis":round(sis)}
    # Indicador final
    ind={}
    for p in PAISES:
        ind[p]=round((sub1[p]["v"]+sub2[p]["v"])/2)
    return sub1,sub2,ind,rc

if __name__=="__main__":
    casos=load_casos()
    sub1,sub2,ind,rc=compute_full(casos)
    oficial_sub2={"AR":0,"BO":23,"BR":100,"CL":59,"CO":100,"CR":53,"CU":0,"DO":28,"EC":18,
                  "GT":33,"HN":52,"JM":0,"MX":37,"PA":0,"PE":51,"PY":0,"SV":0,"UY":0,"VE":0}
    oficial_ind={"AR":0,"BO":30,"BR":76,"CL":57,"CO":85,"CR":46,"CU":0,"DO":30,"EC":25,
                 "GT":32,"HN":42,"JM":0,"MX":47,"PA":0,"PE":53,"PY":0,"SV":0,"UY":0,"VE":0}
    print("VALIDACIÓN SUB2 e INDICADOR FINAL contra oficial 2025")
    print(f"{'País':<5}{'Sub2':>6}{'OfS2':>6}{'OK':>4}{'   ':<3}{'Ind':>5}{'OfInd':>7}{'OK':>4}")
    s2ok=True; iok=True
    for p in PAISES:
        o2=oficial_sub2[p]; oi=oficial_ind[p]
        c2=sub2[p]["v"]; ci=ind[p]
        k2=abs(c2-o2)<=2; ki=abs(ci-oi)<=2
        if not k2: s2ok=False
        if not ki: iok=False
        print(f"{p:<5}{c2:>6}{o2:>6}{'✓' if k2 else '✗':>4}{'   ':<3}{ci:>5}{oi:>7}{'✓' if ki else '✗':>4}")
    print(f"\nSub2: {'OK' if s2ok else 'DISCREPANCIAS'}  |  Indicador: {'OK' if iok else 'DISCREPANCIAS'}")
