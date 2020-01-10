import React from "react";

export default function Step1({ language, setLanguage }) {
  const setBr = () => setLanguage('br');
  const setEn = () => setLanguage('en');
  const setNl = () => setLanguage('nl');

  return (
    <div id="language-picker">
        <a href="#" className={language === 'br' && 'active'} onClick={setBr}>BR</a>
        <a href="#" className={language === 'en' && 'active'} onClick={setEn}>EN</a>
        <a href="#" className={language === 'nl' && 'active'} onClick={setNl}>NL</a>
    </div>
  );
}
