# gunicorn.conf.py
# This is a Python file, so you can use variables and logic if needed.

# The socket to bind to.
# A UNIX socket is generally faster and more secure than a TCP socket (e.g., 127.0.0.1:8000).
# Nginx will communicate with Gunicorn through this file.
bind = "unix:/run/gunicorn.sock"

# The number of worker processes. A common recommendation is (2 * number_of_cores) + 1.
# Start with 3 and adjust based on server performance.
workers = 3

# The user and group to run the Gunicorn process as.
# This should be a non-root user for security. 'www-data' is common on Debian/Ubuntu.
#user = "www-data"
#group = "www-data"

# Logging settings
# Redirect stdout/stderr to the main Gunicorn log file.
capture_output = True
# The location to log errors. '-' means stderr, which will be captured by systemd.
errorlog = "/var/log/gunicorn/error.log"
# The granularity of the error log.
loglevel = "info"
