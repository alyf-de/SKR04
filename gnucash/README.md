
### Flatten CoA

`gnucash_skr*.json` to `gnucash_flat_skr*.json`:

```jq
."gnc-account-example".account | map( {"country_code": "", "name": "Kontenrahmen", "description": "", (.id.__text): {"is_group": (if .code == null then 1 else 0 end  ), "account_number": .code.__text, "name": .name.__text, "account_type": .type.__text, "description": .description.__text, "parent": .parent.__text} } ) |  add
```

### Source

* [SKR03](https://github.com/Gnucash/gnucash/blob/maint/data/accounts/de_DE/acctchrt_skr03.gnucash-xea)
* [SKR04](https://github.com/Gnucash/gnucash/blob/maint/data/accounts/de_DE/acctchrt_skr04.gnucash-xea)

Transform XML to JSON: https://codebeautify.org/xmltojson
