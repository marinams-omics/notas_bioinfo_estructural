#!/usr/bin/env python3
from pathlib import Path
import re, argparse

def extract_model(in_pdb: Path, model_name: str, out_pdb: Path):
    name_re = re.compile(r"^REMARK\s+Name:\s+(\S+)")
    in_target = False
    found = False
    out = []

    for line in in_pdb.read_text(errors="replace").splitlines(True):
        m = name_re.match(line)
        if m:
            in_target = (m.group(1) == model_name)
            if in_target:
                found = True
            continue

        if in_target:
            if line.startswith("ENDMDL"):
                break
            if line.startswith("ATOM"):
                out.append(line)

    if not found:
        raise SystemExit(f"No encontré REMARK Name: {model_name} en {in_pdb}")
    if not out:
        raise SystemExit(f"Encontré {model_name} pero no extraje ATOMs.")

    out.append("TER\nEND\n")
    out_pdb.write_text("".join(out))
    print(f"OK: wrote {out_pdb}")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="inp", required=True)
    ap.add_argument("--name", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    extract_model(Path(args.inp), args.name, Path(args.out))

if __name__ == "__main__":
    main()
