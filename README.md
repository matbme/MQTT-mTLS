```bash
openssl req -new -x509 -days 365 -keyout ca.key -out ca.crt
```

```bash
# Preencher as informações, se deixar em branco da erro
openssl req -new -nodes -out client.csr -keyout client.key
```

```bash
openssl x509 -req -in client.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out client.crt -days 365
```
