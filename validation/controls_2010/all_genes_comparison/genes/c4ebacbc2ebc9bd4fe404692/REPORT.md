# YLR049C
Status: ok. Length: 1319 nt. Measured usable bases: 591. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 591 | 0.2246 | 0.2237 |
| rnafold | ok | 591 | 0.2271 | 0.2310 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 55 | 0.3425 | 0.4619 |
| seed_p | 55 | -0.1748 | 0.0810 |
| seed_p_vs_seed_pars | 49 | -0.1902 | -0.0439 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
