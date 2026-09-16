# YOL139C
Status: ok. Length: 797 nt. Measured usable bases: 682. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 682 | 0.4386 | 0.4358 |
| rnafold | ok | 682 | 0.3391 | 0.3363 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 622 | -0.1058 | -0.1843 |
| seed_p | 622 | -0.0421 | -0.0902 |
| seed_p_vs_seed_pars | 572 | -0.2863 | -0.2601 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
