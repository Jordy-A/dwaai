import React from "react";

export default function Step4(props) {
  const renderResult = (result) => {
    if(result >= 80){
      return <span>
                <span role="img" aria-label="party popper">🎉</span>
                  Yes, you are!
                <span role="img" aria-label="party popper">🎉</span>
            </span>;
    }else if(result>=30){
      return <span>
                <span role="img" aria-label="clapping hands">👏</span>
                  That's quite okay!
                <span role="img" aria-label="clapping hands">👏</span>
            </span>;
    }else{
      return <span>
                <span role="img" aria-label="raising hands">🙌</span>
                  Not yet, but getting there!
                <span role="img" aria-label="raising hands">🙌</span>
            </span>;
    }
  }

  return (
    <div>
      <h1 className="style-font">{ renderResult(props.recordingResult) }</h1>
      <h2>Your score is { props.recordingResult }%</h2>
      <button className="style-font" onClick={() => props.setStep(3)}>&#8634; Retry</button>
      <button className="style-font" onClick={() => props.setStep(1)}>Stop</button>
    </div>
  );
}
