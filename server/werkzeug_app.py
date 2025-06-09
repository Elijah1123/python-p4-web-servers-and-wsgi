#!/usr/bin/env python3
from werkzeug.wrappers import Request, Response

@Request.application
def application(request):
    print(f'This web sever is running at {request.host}')
    return Response('A WSGI generated thi response!')

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple(
         hostname= 'localhost',
         port= 5555,
        application=application,
    )
    # run_simple('
