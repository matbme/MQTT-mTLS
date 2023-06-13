Certificado de CA, Autoridade Certificadora (preencher as informações, se deixar em branco não gera os arquivos):

```bash
openssl req -new -x509 -days 365 -extensions v3_ca -keyout ca.key -out ca.crt
```

Para rodar o comando acima sem o erro `error Loading extension section v3_ca`, foi necessário no arquivo `/etc/ssl/openssl.cnf`, adicionar:

```
[ v3_ca ]
basicConstraints = critical,CA:TRUE
subjectKeyIdentifier = hash
authorityKeyIdentifier = keyid:always,issuer:always
```

Gerar certificado de cliente assinado pela CA (preencher as informações, se deixar em branco não gera os arquivos):

```bash
openssl req -new -nodes -out client.csr -keyout client.key
openssl x509 -req -in client.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out client.crt -days 365
```
