# YBR164C
Status: ok. Length: 766 nt. Measured usable bases: 410. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 410 | 0.4430 | 0.4206 |
| rnafold | ok | 410 | 0.4402 | 0.4220 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 162 | 0.0537 | -0.1599 |
| seed_p | 162 | -0.0192 | -0.2531 |
| seed_p_vs_seed_pars | 115 | -0.1143 | -0.1003 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
