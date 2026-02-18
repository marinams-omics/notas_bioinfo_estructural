#!/usr/bin/env python3
from pathlib import Path
import argparse

def extract_chain(in_pdb: Path, chain: str, out_pdb: Path):
    chain = chain.strip()
    kept = 0
    with in_pdb.open("r", encoding="utf-8", errors="replace") as fin, \
         out_pdb.open("w", encoding="utf-8") as fout:
        for line in fin:
            rec = line[:6]
            if rec in ("ATOM  ", "HETATM"):
                if len(line) > 21 and line[21] == chain:
                    fout.write(line)
                    kept += 1
            elif line.startswith("END"):
                # ignore END from original; we'll add ours
                continue

        fout.write("TER\nEND\n")

    if kept == 0:
        raise SystemExit(
            f"No se escribió nada. ¿Seguro que {in_pdb.name} tiene cadena '{chain}'?"
        )

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="inp", required=True)
    ap.add_argument("--chain", required=True)
    ap.add_argument("--out", dest="out", required=True)
    args = ap.parse_args()

    extract_chain(Path(args.inp), args.chain, Path(args.out))
    print(f"OK: wrote {args.out}")

if __name__ == "__main__":
    main()
