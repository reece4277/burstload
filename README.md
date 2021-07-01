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
