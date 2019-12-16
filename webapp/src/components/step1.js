import React from "react";

export default function Step1(props) {
  return (
    <div>
      <h1 className="style-font">
        Bende gij een Brabander?
      </h1>
      <p>
        Pronounce the sentence above in your best Brabants accent and find out!
      </p>
      <button className="style-font" onClick={() => props.setStep(2)}>Start now!</button>
    </div>
  );
}
