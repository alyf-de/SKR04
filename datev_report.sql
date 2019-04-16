/* Query Report zum Export als CSV und Import in DATEV Software */
select
    gl.posting_date as 'Belegdatum:Date',
    coalesce(acc.account_number, acc_pa.account_number) as Kontonummer,
    coalesce(acc_against.account_number, acc_against_pa.account_number) as 'Gegenkonto (ohne BU-Schlüssel)',
    case gl.debit when 0 then gl.credit else gl.debit end as 'Umsatz (ohne Soll/Haben-Kz):Currency',
    case gl.debit when 0 then 'H' else 'S' end as 'Soll/Haben-Kennzeichen'

from `tabGL Entry` gl
    /* Statistisches Konto (Debitoren/Kreditoren) */
    left join `tabParty Account` pa
    on gl.against = pa.parent
    
    /* Kontonummer */
    left join `tabAccount` acc 
    on gl.account = acc.name

    /* Gegenkonto-Nummer */
    left join `tabAccount` acc_against 
    on gl.against = acc_against.name
    
    /* Statistische Kontonummer */
    left join `tabAccount` acc_pa
    on pa.account = acc_pa.name

    /* Statistische Gegenkonto-Nummer */
    left join `tabAccount` acc_against_pa 
    on pa.account = acc_against_pa.name

where gl.company = '{My Company Here}'
order by 'Belegdatum:Date', voucher_no
