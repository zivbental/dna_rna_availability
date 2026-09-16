# YPL078C
Status: ok. Length: 1021 nt. Measured usable bases: 769. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 769 | 0.2894 | 0.2846 |
| rnafold | ok | 769 | 0.2272 | 0.2265 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 512 | -0.1417 | -0.2416 |
| seed_p | 512 | -0.2420 | -0.2397 |
| seed_p_vs_seed_pars | 423 | -0.2409 | -0.2138 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
