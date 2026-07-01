#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
calc_preliminar.py — Cálculo PRELIMINAR del indicador (escenario "todos entran").

Situación IDEAL / cota superior: toma los casos marcados SI o DUDA en las fichas
(data/fichas/*_detalle.json), asume que TODOS entran (las DUDAs -> SI, sin aplicar
las exclusiones manuales pendientes) y respeta solo el dedup (cuenta_como_iniciativa
= False no se cuenta como iniciativa aparte). Corre el motor 2026 (metodología CENIA
v2) y escribe una planilla nueva con el desglose por país.

NO es el número final: es la foto optimista para dimensionar el techo del indicador.

Salida: data/gates/calculo_preliminar_ILIA2026.xlsx
"""
from __future__ import annotations
import glob, json, os, sys
import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill, Border, Side
from openpyxl.utils import get_column_letter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import calc_engine as ce  # noqa: E402
import export_planilla_simple as eps  # noqa: E402  (reclasificación: criterio corregido)

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

AZUL=PatternFill("solid",fgColor="1F4E78"); VERDE=PatternFill("solid",fgColor="C6EFCE")
AMBARH=PatternFill("solid",fgColor="FFF2CC"); GRIS=PatternFill("solid",fgColor="D9D9D9")
WB=Font(bold=True,color="FFFFFF")
CEN=Alignment(horizontal="center",vertical="center",wrap_text=True)
TL=Alignment(horizontal="left",vertical="top",wrap_text=True)
TH=Side(style="thin",color="BFBFBF"); BOR=Border(left=TH,right=TH,top=TH,bottom=TH)

PAIS_NOMBRE={"AR":"Argentina","BO":"Bolivia","BR":"Brasil","CL":"Chile","CO":"Colombia",
 "CR":"Costa Rica","CU":"Cuba","DO":"Rep. Dominicana","EC":"Ecuador","GT":"Guatemala",
 "HN":"Honduras","JM":"Jamaica","MX":"México","PA":"Panamá","PE":"Perú","PY":"Paraguay",
 "SV":"El Salvador","TT":"Trinidad y Tobago","UY":"Uruguay","VE":"Venezuela"}

# tipo_desarrollador_IA (vocabulario de fichas) -> palabra que entiende norm_dev (legacy)
DEV_FICHA={"privado":"industria","empresa":"industria","academia":"academia",
           "universidad":"academia","gobierno":"gobierno","sociedad civil":"sociedad civil"}


def off(d): return str(d.get("veredicto_equipo") or d.get("entra_tentativo") or "")
def is_in(d): return off(d).upper().startswith(("SI","DUDA"))


def _year(v):
    for x in (v if isinstance(v,list) else [v]):
        try: return int(float(str(x).strip()))
        except (ValueError, TypeError): continue
    return None


def _dev(v):
    return ", ".join(DEV_FICHA.get(str(x).lower().strip(), str(x)) for x in ce._as_list(v))


def ficha_a_caso(d):
    """Mapea una ficha al dict que esperan compute_2026 / raw_counts."""
    return {
        "pais": d.get("pais"), "caso": d.get("nombre_caso") or d.get("caso_id"),
        "ano": _year(d.get("ano_inicio")),
        "tipo_proceso": d.get("tipo_proceso") or [],
        "etapa": d.get("etapas_uso_IA") or [],
        "tipo_convocante": d.get("tipo_convocante") or [],
        "nivel_consolidacion": d.get("nivel_consolidacion"),
        "rol_IA": d.get("rol_IA") or "contenido",
        # --- campos que raw_counts (Sub2) lee por acceso directo ---
        "continuidad": "", "tipo_org": ", ".join(ce._as_list(d.get("tipo_organizacion"))),
        "desarrollador": _dev(d.get("tipo_desarrollador_IA")),
        "origen": d.get("origen_desarrollador") or "",
        "tipos_ia": d.get("tipos_IA_familia") or [],
    }


def cargar_config():
    import yaml
    with open(os.path.join(ROOT,"config.yaml"),encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def hdr(ws,n,h=28):
    for c in range(1,n+1):
        cell=ws.cell(row=1,column=c); cell.fill=AZUL; cell.font=WB; cell.alignment=CEN; cell.border=BOR
    ws.row_dimensions[1].height=h; ws.freeze_panes="A2"


def body(ws,ncol):
    for r in range(2,ws.max_row+1):
        for c in range(1,ncol+1):
            ws.cell(row=r,column=c).alignment=TL; ws.cell(row=r,column=c).border=BOR


def widths(ws,wl):
    for i,w in enumerate(wl,1): ws.column_dimensions[get_column_letter(i)].width=w


def _calc(fichas, keep_ids, cfg):
    """compute_2026 sobre las fichas cuyos caso_id ∈ keep_ids, respetando dedup."""
    efectivos=[d for d in fichas if d["caso_id"] in keep_ids and d.get("cuenta_como_iniciativa") is not False]
    sub1,sub2,ind,_=ce.compute_2026([ficha_a_caso(d) for d in efectivos],cfg)
    con=[p for p in ce.PAISES if sub1[p]["n"]>0]
    return sub1,sub2,ind,efectivos,con


def _prom(ind):
    reg=round(sum(ind[p] for p in ce.PAISES)/len(ce.PAISES))
    con=[p for p in ce.PAISES if ind[p]>0]
    return reg,(round(sum(ind[p] for p in con)/len(con)) if con else 0)


def main():
    cfg=cargar_config()
    fichas=[json.load(open(f,encoding="utf-8")) for f in sorted(glob.glob(os.path.join(ROOT,"data/fichas/*_detalle.json")))]
    IN=[d for d in fichas if is_in(d)]
    in_ids={d["caso_id"] for d in IN}
    dropped=[d for d in IN if d.get("cuenta_como_iniciativa") is False]

    # --- Conjuntos por escenario (criterio corregido jul-2026) ---
    excl=set(eps.EXCLUIR)                                       # 7 confirmados NO
    borderline=set(eps.RECLASIF_DUDA)|set(eps.REVISAR_ENTRA)   # frontera civic-tech ↔ participación
    duda_campo={d["caso_id"] for d in IN if eps.is_duda(d) and d["caso_id"] not in eps.RECLASIF_DUDA}

    techo_ids   = in_ids                                        # todos entran (cota superior)
    central_ids = in_ids - excl                                 # criterio corregido (incluye frontera)
    conserv_ids = in_ids - excl - borderline - duda_campo       # solo ENTRA firmes (cota inferior)

    S_techo   = _calc(fichas, techo_ids,   cfg)
    S_central = _calc(fichas, central_ids, cfg)
    S_conserv = _calc(fichas, conserv_ids, cfg)

    sub1,sub2,ind,efectivos,con_casos = S_central              # el CENTRAL es el principal
    orden=sorted(con_casos,key=lambda p:-ind[p])
    prom_region,prom_con=_prom(ind)
    n_techo=len(S_techo[3]); n_central=len(efectivos); n_conserv=len(S_conserv[3])

    wb=Workbook(); wb.remove(wb.active)

    # ---------- 1 · Resumen (CENTRAL, criterio corregido) ----------
    ws=wb.create_sheet("1 · Resumen (indicador)")
    ws.append(["País","","Sub-Uso","Sub-Desarrollo","INDICADOR","Nº iniciativas"])
    for p in orden:
        ws.append([p,PAIS_NOMBRE[p],round(sub1[p]["v_pub"]),round(sub2[p]["v_pub"]),ind[p],sub1[p]["n"]])
    ws.append([])
    ws.append(["","Promedio (países con iniciativas)","","",prom_con,n_central])
    ws.append(["","Promedio regional (20 países, 0 si no hay)","","",prom_region,""])
    hdr(ws,6); widths(ws,[6,40,12,15,12,14]); body(ws,6)
    for r in range(2,ws.max_row+1):
        for c in (3,4,5,6): ws.cell(row=r,column=c).alignment=CEN
        iv=ws.cell(row=r,column=5)
        if isinstance(iv.value,int):
            iv.font=Font(bold=True)
            if iv.value>=50: iv.fill=VERDE
            elif iv.value>=25: iv.fill=AMBARH
    ws["E1"].fill=AZUL

    # ---------- 2 · Sub1 (Uso) ----------
    ws2=wb.create_sheet("2 · Sub-Uso (5 variables)")
    ws2.append(["País","","Tipos proc.","Etapas","Continuidad","Org. Convocante","Cantidad",
                "Sub-Uso","Nº inic.","Nivel máx","Combos co-conv."])
    for p in orden:
        d=sub1[p]
        ws2.append([p,PAIS_NOMBRE[p],round(d["tipos"]),round(d["etapas"]),round(d["cont"]),
                    round(d["conv"]),round(d["cant"]),round(d["v"]),d["n"],
                    d.get("nivel_max",""),d.get("co_combos","")])
    hdr(ws2,11); widths(ws2,[6,30,11,9,12,15,10,10,9,10,14]); body(ws2,11)
    for r in range(2,ws2.max_row+1):
        for c in range(3,12): ws2.cell(row=r,column=c).alignment=CEN

    # ---------- 3 · Sub2 (Desarrollo) ----------
    ws3=wb.create_sheet("3 · Sub-Desarrollo")
    ws3.append(["País","","Desarrollador (nac/int)","Tipos de IA","Sub-Desarrollo"])
    for p in orden:
        d=sub2[p]
        ws3.append([p,PAIS_NOMBRE[p],round(d["dev"]),round(d["sis"]),round(d["v"])])
    hdr(ws3,5); widths(ws3,[6,30,22,14,16]); body(ws3,5)
    for r in range(2,ws3.max_row+1):
        for c in (3,4,5): ws3.cell(row=r,column=c).alignment=CEN

    # ---------- 4 · Escenarios (techo / central / conservador) ----------
    wsE=wb.create_sheet("4 · Escenarios (rango)")
    i_t,i_c,i_v=S_techo[2],S_central[2],S_conserv[2]
    pt=_prom(i_t); pc=_prom(i_c); pv=_prom(i_v)
    wsE.append(["Escenario","Qué incluye","Nº inic.","Prom. regional (20)","Prom. países con casos"])
    wsE.append(["TECHO (todos entran)","Todos los SI/DUDA; ignora el criterio corregido",n_techo,pt[0],pt[1]])
    wsE.append(["CENTRAL (criterio corregido)","Saca los 7 no-participación; mantiene la frontera y DUDAs",n_central,pc[0],pc[1]])
    wsE.append(["CONSERVADOR","Solo ENTRA firmes; saca frontera y DUDAs sin resolver",n_conserv,pv[0],pv[1]])
    wsE.append([])
    wsE.append(["Indicador por país","","TECHO","CENTRAL","CONSERVADOR"])
    for p in sorted([q for q in ce.PAISES if i_t[q]>0],key=lambda q:-i_c[q]):
        wsE.append([p,PAIS_NOMBRE[p],i_t[p],i_c[p],i_v[p]])
    hdr(wsE,5); widths(wsE,[26,48,9,18,20]); body(wsE,5)
    for r in range(2,wsE.max_row+1):
        for c in (3,4,5): wsE.cell(row=r,column=c).alignment=CEN
    for r in (2,3,4):
        wsE.cell(row=r,column=1).font=Font(bold=True)
    wsE.cell(row=3,column=1).fill=VERDE   # central resaltado

    # ---------- 5 · Casos incluidos (central) ----------
    ws4=wb.create_sheet("5 · Casos incluidos (central)")
    ws4.append(["País","Caso","¿ENTRA? (equipo)","Tipo de proceso","Etapas uso IA","Nivel",
                "Convocante(s)","Desarrollador","Origen","Tipos de IA"])
    for d in sorted(efectivos,key=lambda x:(str(x.get("pais")),str(x.get("nombre_caso")))):
        j=lambda v:"; ".join(map(str,v)) if isinstance(v,list) else ("" if v is None else str(v))
        ws4.append([d.get("pais"),d.get("nombre_caso"),d.get("veredicto_equipo") or d.get("entra_tentativo") or "",
                    j(d.get("tipo_proceso")),j(d.get("etapas_uso_IA")),
                    "" if d.get("nivel_consolidacion") is None else d.get("nivel_consolidacion"),
                    j(d.get("tipo_convocante")),j(d.get("tipo_desarrollador_IA")),
                    d.get("origen_desarrollador") or "",j(d.get("tipos_IA_familia"))])
    hdr(ws4,10); widths(ws4,[6,34,15,22,20,7,24,16,16,26]); body(ws4,10)

    # ---------- 6 · Supuestos y método ----------
    ws5=wb.create_sheet("6 · Supuestos y método")
    dup_txt="; ".join(f"{d.get('pais')} {d.get('nombre_caso')}" for d in dropped) or "—"
    filas=[
     ["CÁLCULO PRELIMINAR — criterio corregido (jul-2026). Escenario CENTRAL + rango [conservador–techo]"],
     ["",""],
     ["Qué es",f"Preliminar y determinístico, para dimensionar el indicador. El principal es el CENTRAL "
              f"({n_central} iniciativas). NO es el número final: sale tras la validación manual (pestaña 2)."],
     ["Criterio de elegibilidad","Un caso ENTRA si es realmente un proceso de PARTICIPACIÓN CIUDADANA con IA en "
              "alguna etapa (incl. logística: modera/administra turnos/prepara materiales). NO entra civic tech "
              "(reporte/servicio/monitoreo), atención ciudadana ni voto/conteo electoral. La IA no necesita analizar el contenido."],
     ["",""],
     ["Escenario TECHO",f"{n_techo} iniciativas. Todos los SI/DUDA entran (ignora el criterio). Cota superior."],
     ["Escenario CENTRAL",f"{n_central} iniciativas. Saca los {len(excl)} confirmados no-participación; MANTIENE la "
              "frontera (Chatico, Colab) y todas las DUDAs. Es el escenario principal de esta planilla."],
     ["Escenario CONSERVADOR",f"{n_conserv} iniciativas. Solo los ENTRA firmes: saca además la frontera y las DUDAs "
              "sin resolver. Cota inferior."],
     ["Excluidos (criterio)",f"{len(excl)} confirmados NO: "+", ".join(sorted(excl))],
     ["Dedup",f"Se respeta: {len(dropped)} duplicado no se cuenta aparte → {dup_txt}."],
     ["",""],
     ["Metodología","CENIA v2 (jun-2026). Indicador = (Sub-Uso + Sub-Desarrollo) / 2."],
     ["Sub-Uso","Promedio de 5: Tipos de proceso (÷5) · Etapas (÷4) · Continuidad = nivel máx. del país (÷3) · "
              "Organización Convocante (3 sub-componentes: gub ÷3 + no-gub ÷4 + co-convocatoria por máx. relativo) · "
              "Cantidad = todas las elegibles (umbrales 0/25/50/75/100)."],
     ["Sub-Desarrollo","Idéntico a 2025: desarrollador nacional/internacional × 4 tipos (máx. relativo) + tipos de IA."],
     ["Redondeo",f"{cfg.get('redondeo',{}).get('modo','legacy')} · count_min_level="
              f"{cfg.get('cantidad',{}).get('count_min_level',0)} · escenario={cfg.get('escenarios',{}).get('scenario_activo','A')}"],
     ["",""],
     ["Resultado CENTRAL",f"Prom. regional {prom_region} (media de 20) · prom. {prom_con} entre los {len(con_casos)} países con iniciativas."],
     ["Aviso","El número final se obtiene tras la validación manual (pestaña 2 de la planilla principal) "
              "resolviendo la frontera y las DUDAs, y volviendo a correr el motor."],
    ]
    for row in filas: ws5.append(row)
    ws5.column_dimensions["A"].width=24; ws5.column_dimensions["B"].width=112
    for r in range(1,ws5.max_row+1):
        ws5.cell(row=r,column=1).font=Font(bold=True); ws5.cell(row=r,column=1).alignment=TL
        ws5.cell(row=r,column=2).alignment=TL
    ws5["A1"].font=Font(bold=True,size=12)

    dst=os.path.join(ROOT,"data/gates/calculo_preliminar_ILIA2026.xlsx"); wb.save(dst)
    print(f"[ok] {dst}")
    print(f"     CENTRAL: {n_central} inic · {len(con_casos)} países · prom regional={prom_region} · prom con casos={prom_con}")
    print(f"     rango regional: techo={_prom(i_t)[0]} (n={n_techo}) · central={prom_region} (n={n_central}) · conservador={_prom(i_v)[0]} (n={n_conserv})")
    print("\n     País  Sub-Uso  Sub-Des  Indicador  n")
    for p in orden:
        print(f"     {p:>3}   {round(sub1[p]['v_pub']):>5}   {round(sub2[p]['v_pub']):>5}   "
              f"{ind[p]:>7}   {sub1[p]['n']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
