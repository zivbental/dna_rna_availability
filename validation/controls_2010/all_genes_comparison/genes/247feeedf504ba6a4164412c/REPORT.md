# YCR004C
Status: ok. Length: 1080 nt. Measured usable bases: 780. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 780 | 0.2958 | 0.2789 |
| rnafold | ok | 780 | 0.2738 | 0.2591 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 625 | 0.0450 | -0.1368 |
| seed_p | 625 | 0.0142 | -0.0047 |
| seed_p_vs_seed_pars | 487 | 0.0039 | -0.0429 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
