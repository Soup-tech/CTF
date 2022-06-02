```
[*] Service scan get-arch (tcp/135/msrpc/get-arch) ran a command which returned a non-zero exit code (1).
[-] Command: getArch.py -target 10.10.10.134
[-] Error Output:
/usr/lib/python3/dist-packages/pkg_resources/__init__.py:116: PkgResourcesDeprecationWarning: 1.16.0-unknown is an invalid version and will not be supported in a future release
  warnings.warn(
/usr/lib/python3/dist-packages/pkg_resources/__init__.py:116: PkgResourcesDeprecationWarning: 1.12.1-git20200711.33e2d80-dfsg1-0.6 is an invalid version and will not be supported in a future release
  warnings.warn(
Traceback (most recent call last):
  File "/usr/lib/python3/dist-packages/pkg_resources/__init__.py", line 573, in _build_master
    ws.require(__requires__)
  File "/usr/lib/python3/dist-packages/pkg_resources/__init__.py", line 891, in require
    needed = self.resolve(parse_requirements(requirements))
  File "/usr/lib/python3/dist-packages/pkg_resources/__init__.py", line 782, in resolve
    raise VersionConflict(dist, req).with_context(dependent_req)
pkg_resources.VersionConflict: (impacket 0.10.0 (/usr/lib/python3/dist-packages), Requirement.parse('impacket==0.9.25.dev1+20220218.140931.6042675a'))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/usr/local/bin/getArch.py", line 4, in <module>
    __import__('pkg_resources').run_script('impacket==0.9.25.dev1+20220218.140931.6042675a', 'getArch.py')
  File "/usr/lib/python3/dist-packages/pkg_resources/__init__.py", line 3267, in <module>
    def _initialize_master_working_set():
  File "/usr/lib/python3/dist-packages/pkg_resources/__init__.py", line 3241, in _call_aside
    f(*args, **kwargs)
  File "/usr/lib/python3/dist-packages/pkg_resources/__init__.py", line 3279, in _initialize_master_working_set
    working_set = WorkingSet._build_master()
  File "/usr/lib/python3/dist-packages/pkg_resources/__init__.py", line 575, in _build_master
    return cls._build_from_requirements(__requires__)
  File "/usr/lib/python3/dist-packages/pkg_resources/__init__.py", line 588, in _build_from_requirements
    dists = ws.resolve(reqs, Environment())
  File "/usr/lib/python3/dist-packages/pkg_resources/__init__.py", line 777, in resolve
    raise DistributionNotFound(req, requirers)
pkg_resources.DistributionNotFound: The 'impacket==0.9.25.dev1+20220218.140931.6042675a' distribution was not found and is required by the application


[*] Service scan Enum4Linux (tcp/139/netbios-ssn/enum4linux) ran a command which returned a non-zero exit code (1).
[-] Command: enum4linux -a -M -l -d 10.10.10.134 2>&1
[-] Error Output:


[*] Service scan wkhtmltoimage (tcp/5985/http/wkhtmltoimage) ran a command which returned a non-zero exit code (1).
[-] Command: wkhtmltoimage --format png http://10.10.10.134:5985/ /home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/tcp5985/tcp_5985_http_screenshot.png
[-] Error Output:
QStandardPaths: XDG_RUNTIME_DIR not set, defaulting to '/tmp/runtime-root'
Loading page (1/2)
[>                                                           ] 0%
Error: Failed to load http://10.10.10.134:5985/, with network status code 203 and http status code 404 - Error transferring http://10.10.10.134:5985/ - server replied: Not Found
[==============================>                             ] 50%
[============================================================] 100%
Rendering (2/2)
[>                                                           ] 0%
[===============>                                            ] 25%
[============================================================] 100%
Done
Exit with code 1 due to network error: ContentNotFoundError


[*] Service scan wkhtmltoimage (tcp/47001/http/wkhtmltoimage) ran a command which returned a non-zero exit code (1).
[-] Command: wkhtmltoimage --format png http://10.10.10.134:47001/ /home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/tcp47001/tcp_47001_http_screenshot.png
[-] Error Output:
QStandardPaths: XDG_RUNTIME_DIR not set, defaulting to '/tmp/runtime-root'
Loading page (1/2)
[>                                                           ] 0%
Error: Failed to load http://10.10.10.134:47001/, with network status code 203 and http status code 404 - Error transferring http://10.10.10.134:47001/ - server replied: Not Found
[==============================>                             ] 50%
[============================================================] 100%
Rendering (2/2)
[>                                                           ] 0%
[===============>                                            ] 25%
[============================================================] 100%
Done
Exit with code 1 due to network error: ContentNotFoundError



```