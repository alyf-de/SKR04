> UNDER DEVELOPMENT. This has NOT been tested. Use with care.

Standardkontenrahmen 04 for ERPNext.

Sponsored by [//SEIBERT/MEDIA](https://www.seibert-media.net/) and [tüit](https://www.tueit.de/).

### Testen 

```bash
scp de_skr_hgb.json my.erp.com:/home/frappe/frappe-bench/apps/erpnext/erpnext/accounts/doctype/account/chart_of_accounts/verified/
ssh my.erp.com
cd frappe-bench/ && bench clear-cache
```

### Notizen

* Die Länge der Kontennamen ist auf 140 Zeichen beschränkt.
* Die führenden Nummern der Wurzel- und Gruppenkonten stammen aus dem Handelsgesetzbuch. Sie sind nur für den Jahresabschluss relevant.

### License

Copyright (C) 2019 Raffael Meyer raffael@alyf.de

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see https://www.gnu.org/licenses/.
