
### Flatten CoA

https://jqplay.org/

* Filter:

```jq
  ."gnc-account-example".account | map( {"country_code": "", "name": "Kontenrahmen", "description": "", (.id.__text): {"is_group": (if .code == null then 1 else 0 end  ), "account_number": .code.__text, "name": .name.__text, "account_type": .type.__text, "description": .description.__text, "parent": .parent.__text} } ) |  add
```

* JSON: `gnucash_skr*.json`
* Result: `gnucash_skr*_flat.json`

---

* Filter:

```jq
  ."gnc-account-example".account | map( [ {"id": .id.__text, "is_group": (if .code == null then 1 else 0 end  ), "account_number": .code.__text, "name": .name.__text, "account_type": .type.__text, "description": .description.__text, "parent": .parent.__text} ] ) |  add
```

* JSON: `gnucash_skr*.json`
* Result: `gnucash_skr*_array.json`

### Nesting

```bash
python main.py
```

### Source

* [SKR03](https://github.com/Gnucash/gnucash/blob/maint/data/accounts/de_DE/acctchrt_skr03.gnucash-xea)
* [SKR04](https://github.com/Gnucash/gnucash/blob/maint/data/accounts/de_DE/acctchrt_skr04.gnucash-xea)

Transform XML to JSON: https://codebeautify.org/xmltojson
