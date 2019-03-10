> In Entwicklung. Einsatz in Produktivsystemen derzeit noch nicht empfohlen.

Standardkontenrahmen 04 for ERPNext.

Sponsored by [//SEIBERT/MEDIA](https://www.seibert-media.net/) and [tüit](https://www.tueit.de/).

* `de_skr_hgb.json` enthält die Struktur von Bilanz und GuV-Rechnung nach HGB, **ohne** Konten,
* `de_skr04_hgb.json` enthält die Konten des SKR 04, eingeordnet in die Struktur von Bilanz und GuV-Rechnung nach HGB.

![Struktur des Kontenrahmens](oberkonten.png)


ERPNext bucht nach dem Umsatzkostenverfahren.

Der Kontotyp bewirkt, dass an den entsprechender Stelle in ERPNext nur Konten dieses Typs angeboten werden. Außerdem werden die Standardkonten beim Erstellen eines neuen Unternehmens anhand der Kontentypen gesetzt.

### Testen 

```bash
scp de_skr04_hgb.json my.erp.com:/home/frappe/frappe-bench/apps/erpnext/erpnext/accounts/doctype/account/chart_of_accounts/verified/
ssh my.erp.com
cd frappe-bench/ && bench clear-cache
```

* [More on SCP](https://unix.stackexchange.com/a/106482)
* [More on Bench](https://frappe.io/docs/user/en/bench/resources/bench-commands-cheatsheet)

### Notizen

* Die Konten für Löhne und Gehälter sind unter Herstelllungskosten angesiedelt. Für eine korrekte GuV-Rechnung muss der Personalaufwand für allgemeine Verwaltungskosten und Vertriebskosten umgebucht werden.

* Die Länge der Kontennamen ist auf 140 Zeichen beschränkt.

* Die führenden Nummern der Wurzel- und Gruppenkonten stammen aus dem Handelsgesetzbuch. Sie sind nur für den Jahresabschluss relevant.

#### CSV zu JSON

```csv
1800, Kasse, Cash
1810, Nebenkasse 1
1811, Sparschwein
1820, Nebenkasse 2
```

Sollte zu

```json
{
  "Kasse (Gruppe)" : {
    "is_group" : 1,
    "Kasse" : {
      "account_number" : 1800,
      "account_type" : "Cash"
    },
  "Nebenkasse 1 (Gruppe)" : {
    "is_group": 1,
    "Nebenkasse 1" : {
      "account_number": 1810,
      "account_type": "Cash"
    },
    "Sparschwein" : {
      "account_number": 1811,
      "account_type": "Cash"
    },
  },
  "Nebenkasse 2" : {
    "account_number": 1200,
    "account_type": "Cash"
  }
}
```

werden.

#### Remove Number from Groups

Replace

```regex
"is_group": 1,\n {0,}"account_number": ".{4}"
```

with

```
"is_group": 1
```

### License

Copyright (C) 2019 Raffael Meyer raffael@alyf.de

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see https://www.gnu.org/licenses/.
