# ripenetworkchecker

A tool to check whether a given IP is in a list of CIDR ranges posted by RIPE Networks.

To use: 
------------
```bash
python main.py --ip $IP to check
```

Example:
------------

```python
python main.py --ip 192.168.10.1
IP: 192.168.10.1 is not in the list of cidrs
```
