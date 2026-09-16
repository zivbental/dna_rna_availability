# YHL047C
Status: ok. Length: 1998 nt. Measured usable bases: 890. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 890 | 0.3028 | 0.2850 |
| rnafold | ok | 890 | 0.2383 | 0.2343 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 151 | -0.5603 | -0.5640 |
| seed_p | 151 | -0.6354 | -0.5375 |
| seed_p_vs_seed_pars | 114 | -0.6905 | -0.4182 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
