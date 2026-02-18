#!/usr/bin/env python3
from pathlib import Path
import argparse

def trim_first_n_residues(in_pdb: Path, out_pdb: Path, n: int):
    # Identify residues by (chain, resseq+icode). We'll keep everything AFTER skipping n residues.
    seen = []
    keep_res = set()

    def resid_key(line):
        chain = line[21]
        resseq = line[22:26]   # includes spaces
        icode = line[26]       # insertion code
        return (chain, resseq, icode)

    # First pass: collect residue order (ATOM only)
    for line in in_pdb.read_text(errors="replace").splitlines(True):
        if not (line.startswith("ATOM") or line.startswith("HETATM")):
            continue
        key = resid_key(line)
        if not seen or key != seen[-1]:
            seen.append(key)

    if len(seen) <= n:
        raise SystemExit(f"File has only {len(seen)} residues; cannot trim first {n}.")

    # Residues to keep
    for key in seen[n:]:
        keep_res.add(key)

    # Second pass: write only kept residues’ ATOM/HETATM + TER/END
    out_lines = []
    for line in in_pdb.read_text(errors="replace").splitlines(True):
        if line.startswith(("ATOM", "HETATM")):
            if resid_key(line) in keep_res:
                out_lines.append(line)
        # ignore everything else; we will add TER/END
    out_lines.append("TER\nEND\n")

    out_pdb.write_text("".join(out_lines))
    return len(seen), len(keep_res)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="inp", required=True)
    ap.add_argument("--out", dest="out", required=True)
    ap.add_argument("--n", type=int, required=True, help="number of leading residues to remove")
    args = ap.parse_args()

    inp = Path(args.inp)
    out = Path(args.out)
    total, kept = trim_first_n_residues(inp, out, args.n)
    print(f"OK: {inp} total_res={total} trimmed_first={args.n} kept_res={kept} -> {out}")

if __name__ == "__main__":
    main()
