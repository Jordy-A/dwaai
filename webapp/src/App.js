import React, { useState } from 'react';
import './App.css';
import Step1 from "./components/step1";
import Step2 from "./components/step2";
import Step3 from "./components/step3";
import Step4 from "./components/step4";

function App() {
  const [currentStep, setStep] = useState(1);

  return (
    <div className="App">
      <div className="App-content">
        <img src="/eindhoven-vibes.png" className="App-logo" alt="logo" />

        { currentStep === 1 && <Step1 setStep={setStep} /> }
        { currentStep === 2 && <Step2 setStep={setStep} /> }
        { currentStep === 3 && <Step3 setStep={setStep} /> }
        { currentStep === 4 && <Step4 setStep={setStep} /> }

      </div>
    </div>
  );
}

export default App;
