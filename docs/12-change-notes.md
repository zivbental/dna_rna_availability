# Changes on this branch

This branch adds documentation, experimental comparison tools and saved artifacts
on top of the initial repository import. The production `rnavail` package and its
CLI behavior are unchanged.

## Documentation

- Add a reading guide, glossary and suggested paths for users, reviewers and
  readers seeking the scientific derivations.
- Expand explanations of the question, pipeline, architecture, adapters,
  consensus, scoring, output interpretation and limitations.
- Add mathematical and chemical foundations covering ensembles, partition
  functions, joint opening probability, opening free energy, seeds, sampling,
  consensus, ranking, salt and probing constraints.
- Add a command reference with defaults, recipes, all scan options and a clear
  distinction between modeled conditions and recorded metadata.
- Replace the older implementation proposal with current implementation status
  and a roadmap; update README links and examples to the existing 25-nt window
  and 25-candidate defaults. These are documentation corrections, not new defaults.
- Clarify that single-molecule accessibility and heuristic ranking do not establish
  binding or experimentally calibrated availability.

## Validation and deposited-data comparisons

- Add reproducible synthetic controls and CCW12/RPL41A examples based on the
  deposited Kertesz 2010 GSE22393 PARS dataset, with FASTA inputs, metrics,
  JSON/text/HTML reports, plots and temperature/seed diagnostics.
- Preserve compressed source data, download provenance and SHA256 manifests.
- Add a transcript-wide comparison command and plotting tool. Comparisons report
  per-gene Pearson and tie-aware Spearman correlations, pooled Pearson and median
  per-gene statistics; undefined results remain null.
- Validate transcript sequences against genomic coordinates, including reverse
  strands and exact annotated exon/UTR projections. Preserve missing measurements
  and explicitly handle ambiguous antisense overlaps.
- Compare local RNAplfold and global RNAfold separately. Full-site and best-seed
  window diagnostics are exploratory because PARS does not measure simultaneous
  whole-site opening.
- Support isolated worker processes, atomic per-transcript checkpoints and resume
  checks against settings, source hashes, implementation hashes and tool versions.
- Preserve initial sequential and contiguous-mapping runs alongside the newer
  annotated-block mapping run for provenance.

The transcript-wide run was still executing when this branch was prepared. Its
committed checkpoints are an intermediate snapshot, not a completed dataset-wide
benchmark. Subsequent results generated locally are not part of this commit.
The small control benchmark reports model sanity checks passing, but selected
experimental window ordering agrees for RPL41A and disagrees for CCW12; the
reports describe this limitation explicitly.

## Presentation and examples

- Add AREG and SELE FASTA inputs.
- Add a PowerPoint presentation, its builder, report screenshot capture script
  and image assets. The capture script references a historical local report under
  `runs/`; rebuilding those screenshots requires that report. The saved images
  and presentation are included for viewing without it.
- Presentation tooling uses optional matplotlib, Pillow, python-pptx and
  Playwright dependencies; it does not add production package dependencies.
- Ignore downloaded browser system dependencies and temporary validation
  checkpoint files.

## Verification

The new tests check documentation links and anchors, documented CLI defaults,
scan option coverage, dataset parsing, coordinate projection, missingness,
correlation statistics, pooled moments and best-seed window calculations using
small synthetic fixtures. The full existing suite is run before pushing; the
commit message records its result. Generated TSV files retain their original
CRLF line endings.
