
@echo off

set IXP_HOME=C:\Users\zkxcpjj\Downloads\Autosys_cli\ixp
set PATH=%PATH%;%IXP_HOME%\bin

set AUTOSERV=DA2
set IXP_SERVER_URL=http://amrs-autosys-d.bankofamerica.com
title=%USERNAME%@DA2
prompt=%USERNAME%@DA2$^^G
ixautorep -J HGRX_GRADS_M_IRRBV_UPDATE_PERKEY_DEV3_CM