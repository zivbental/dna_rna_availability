# YIL038C
Status: ok. Length: 2867 nt. Measured usable bases: 1005. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1005 | 0.3073 | 0.2876 |
| rnafold | ok | 1005 | 0.3038 | 0.2905 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 91 | 0.4763 | 0.5984 |
| seed_p | 91 | 0.0844 | 0.1885 |
| seed_p_vs_seed_pars | 76 | 0.1725 | 0.0990 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
