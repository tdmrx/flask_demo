from functools import wraps,partial
from flask import g, request, redirect, url_for,session
import typing
from werkzeug.exceptions import Forbidden

def allow(func: typing.Callable = None, **options: typing.Any) -> typing.Callable:
    if func is None:
        return partial(allow, **options)

    @wraps(func)
    def decorated(*args: typing.Any, **kwargs: typing.Any) -> typing.Any:
        groups = options.get("groups")
        if "role" in session:
            if session["role"] in groups:
                 return func(*args, **kwargs)
        else:
            return redirect(url_for("login.login"))
        raise Forbidden
    return decorated

def deny(func: typing.Callable = None, **options: typing.Any) -> typing.Callable:
    if func is None:
        return partial(deny, **options)

    @wraps(func)
    def decorated(*args: typing.Any, **kwargs: typing.Any) -> typing.Any:
        groups = options.get("groups")
        if "role" in session:
            if session["role"] in groups:
                 raise Forbidden
        else:
            return redirect(url_for("login.login"))
        return func(*args, **kwargs)
 

    return decorated

def logged(func: typing.Callable = None, **options: typing.Any) -> typing.Callable:
    if func is None:
        return partial(logged, **options)

    @wraps(func)
    def decorated(*args: typing.Any, **kwargs: typing.Any) -> typing.Any:
        if "logged" in session:
            return func(*args, **kwargs)
        else:
            return redirect(url_for("login.login"))
    return decorated