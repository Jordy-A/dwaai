import React from "react";
import QrReader from 'react-qr-reader';

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
      <h2>Scan your entry ticket to start</h2>
    </div>
  );
}
