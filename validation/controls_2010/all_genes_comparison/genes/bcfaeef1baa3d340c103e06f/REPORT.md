# YOL057W
Status: ok. Length: 2299 nt. Measured usable bases: 1574. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1574 | 0.3065 | 0.2932 |
| rnafold | ok | 1574 | 0.2624 | 0.2454 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 721 | -0.1382 | -0.1402 |
| seed_p | 721 | -0.2597 | -0.2278 |
| seed_p_vs_seed_pars | 547 | -0.1903 | -0.1925 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
