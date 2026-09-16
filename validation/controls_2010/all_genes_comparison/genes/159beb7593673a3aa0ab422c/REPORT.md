# YLR363W-A
Status: ok. Length: 460 nt. Measured usable bases: 197. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 197 | 0.2935 | 0.2965 |
| rnafold | ok | 197 | 0.2065 | 0.2246 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 54 | -0.1709 | -0.4704 |
| seed_p | 54 | -0.2173 | 0.0277 |
| seed_p_vs_seed_pars | 52 | -0.0061 | 0.1254 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
