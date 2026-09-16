# YMR157C
Status: ok. Length: 890 nt. Measured usable bases: 402. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 402 | 0.2979 | 0.2894 |
| rnafold | ok | 402 | 0.1829 | 0.1867 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 101 | 0.2969 | 0.2739 |
| seed_p | 101 | 0.2402 | 0.3616 |
| seed_p_vs_seed_pars | 87 | 0.2601 | 0.3083 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
