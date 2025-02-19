from flask import jsonify, request
from flask_limiter.util import get_remote_address
import sqlite3
from datetime import datetime, timedelta
from functools import wraps

def rate_limit(max_requests=50, window_minutes=60):
    def decorator(f):
        @wraps(f)
        def wrapped_function(*args, **kwargs):
            ip = get_remote_address()
            endpoint = request.endpoint

            conn = sqlite3.connect('rate_limits.db')
            c = conn.cursor()

            now = datetime.utcnow()
            window_start = now - timedelta(minutes=window_minutes)

            c.execute('''
                SELECT request_count, window_start
                FROM rate_limits
                WHERE ip_address = ? AND endpoint = ?
            ''', (ip, endpoint))

            result = c.fetchone()

            if result:
                count, start_time = result
                start_time = datetime.fromisoformat(start_time)

                if start_time < window_start:
                    c.execute('''
                        UPDATE rate_limits
                        SET request_count = 1, window_start = ?
                        WHERE ip_address = ? AND endpoint = ?
                    ''', (now.isoformat(), ip, endpoint))
                else:
                    if count >= max_requests:
                        conn.close()
                        return jsonify({'error': 'Rate limit exceeded'}), 429

                    c.execute('''
                        UPDATE rate_limits
                        SET request_count = request_count + 1
                        WHERE ip_address = ? AND endpoint = ?
                    ''', (ip, endpoint))
            else:
                c.execute('''
                    INSERT INTO rate_limits (ip_address, endpoint, request_count, window_start)
                    VALUES (?, ?, 1, ?)
                ''', (ip, endpoint, now.isoformat()))

            conn.commit()
            conn.close()

            return f(*args, **kwargs)
        return wrapped_function
    return decorator
