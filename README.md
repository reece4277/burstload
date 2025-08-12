[![Python](https://img.shields.io/badge/python-3.9%2B-blue)]() [![Releases](https://img.shields.io/github/v/release/reece4277/burstload)]() [![License](https://img.shields.io/github/license/reece4277/burstload)]()

# BurstLoad v4.1

**BurstLoad** is a high-concurrency web stress simulator built for developers and sysadmins who want to benchmark and monitor the resilience of their own web services under simulated load.

> Educational use only. Always test responsibly and never target infrastructure you do not own.

## Features
- Threaded, concurrent HTTP requests
- Randomised headers and user-agents
- Realtime response logging and status tracking
- Command-line control over concurrency, delays, and timeouts

## Usage
```bash
python3 burstload.py https://yourdomain.com --threads 50 --delay 0.1 --timeout 5 --log output.log
```

## Changelog
**v4.1**
- Added latency timing per request
- Improved error logging
- Optional log-to-file feature

**v3.5**
- Initial CLI tool with basic threading and user-agent rotation

## License
MIT License

## History
- **v1.0.0** (2018‑06‑20) — First public CLI version
- **v2.0.0** (2019‑07‑12) — Config & header randomization
- **v3.0.0** (2020‑06‑18) — Multi‑threaded load tests
- **v4.0.0** (2023‑09‑14) — Async speed boosts
- **v4.1.0** (2025‑08‑12) — Latest refinements
