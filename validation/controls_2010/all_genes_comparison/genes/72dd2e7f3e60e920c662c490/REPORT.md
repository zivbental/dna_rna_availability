# YER124C
Status: ok. Length: 2060 nt. Measured usable bases: 1370. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1370 | 0.2831 | 0.2629 |
| rnafold | ok | 1370 | 0.2629 | 0.2460 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 774 | 0.0153 | -0.1636 |
| seed_p | 774 | -0.1341 | -0.0763 |
| seed_p_vs_seed_pars | 585 | -0.3548 | -0.2686 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
