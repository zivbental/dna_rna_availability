# YJR145C
Status: ok. Length: 876 nt. Measured usable bases: 193. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 193 | 0.3208 | 0.3175 |
| rnafold | ok | 193 | 0.3241 | 0.3347 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 58 | -0.3694 | -0.5512 |
| seed_p | 58 | -0.5791 | -0.6147 |
| seed_p_vs_seed_pars | 46 | -0.7291 | -0.6909 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
