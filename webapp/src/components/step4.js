import React, { useState, useEffect } from "react";

export default function Step4(props) {
  return (
    <div>
      <h1 className="style-font">
        Yes, you are!
      </h1>
      <button className="style-font" onClick={() => props.setStep(3)}>&#8634; Retry</button>
      <button className="style-font" onClick={() => props.setStep(1)}>Stop</button>
    </div>
  );
}
