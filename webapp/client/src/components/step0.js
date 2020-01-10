import React from "react";
import QrReader from 'react-qr-reader';

const cta = {
  en: 'Scan your entry ticket to start',
  nl: 'Scan uw ticket om te beginnen',
  br: 'Scant ekkes oew ticket, dan beginnen we'
}

export default function Step0(props) {
  const setData = (data) => {
    const integer = parseInt(data);
    console.log('Scanned QR code: ', data, integer);

    // GUARD: QR code must be a number
    if (isNaN(integer)) {
      return;
    }

    // If the QR code contains a number, set the participant ID and open the application.
    props.setParticipantId(+data);
    props.setStep(1);
  }

  return (
    <div id='qr-code-scanner'>
      <QrReader onScan={setData} onError={console.error} />
      <h2>{cta[props.language]}</h2>
    </div>
  );
}
