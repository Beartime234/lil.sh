import React from 'react';
/** @jsx jsx */
import { jsx, css } from '@emotion/core';
import RequestLink from "../components/RequestLink";
import ReactNotification from 'react-notifications-component'
import 'react-notifications-component/dist/theme.css'
import {useThemeContext} from "../contexts/ThemeContext";
import { palette } from '../styles/palette';


const HomePageStyle = (isLight) => css`
  h1 {
    font-size: 5rem;
    font-weight: 600;
    text-align: center;
    margin: .2em 0;
  }
  
  h5 {
    text-align: center;
    margin-bottom: 3rem
  }
  
  .app-body {
    text-align: center;
    margin-top: 5rem
  }
  
  .redirect-form {
    font-size: 1.6rem;
  }

  .redirect-location-input {
    margin-top: 2rem;
    margin-bottom: 1rem;
    text-align: center;
    width: 50rem;
    display: inline-block;
    padding: 12px 20px;
    color: ${isLight ? palette.white[0] : palette.black[0]};
    background-color: ${isLight ? palette.black[0] : palette.white[0]};
  }
  
  .suffix-checkbox {
    margin-top: 1rem;
    margin-bottom: 1rem;
  }
  
  .redirect-location-label {
    display: block;
  }
  
  .suffix-checkbox-label {
    font-size: 1.2rem;
    bottom: .2rem;
    position: relative;
  }
  
  .redirect-location-div {
    margin-bottom: .5rem;
  }
  
  .suffix-checkbox-div {
    margin-top 1rem;
  }
  
  .suffix-div {
    margin-top: 4rem;
    margin-bottom: .5rem;
  }
  
  .generate-button-div {
    margin-top 2rem;
  }
  
  .suffix-input {
    width: 15rem;
    color: ${isLight ? palette.white[0] : palette.black[0]};
    background-color: ${isLight ? palette.black[0] : palette.white[0]}
  }
  
  .app-button {
    color: ${isLight ? palette.white[0] : palette.black[0]} !important;
    text-transform: lowercase;
    text-decoration: none;
    background: ${isLight ? palette.black[0] : palette.white[0]};
    padding: 15px;
    display: inline-block;
    border: none;
    transition: all 0.4s ease 0s;
  }
  
  .app-button:hover {
    cursor: pointer;
  }
  
  .app-button:disabled {
    cursor: not-allowed;
    color: #808080 !important;
  }
  
  .error-message-div {
    color: red;
  }
  
  .yourlink-div {
    font-size: 1.6rem
  }
  
  .make-another-div {
    margin-top: 5rem;
  }
  
  .link-text {
    text-decoration: underline;
    cursor: pointer;
    font-size: 3rem;
  }
`;

const HomePage = () => {
  const { isLight } = useThemeContext();

  return (
    <div css={[HomePageStyle(isLight)]}>
      <ReactNotification />
      <h1 className="title">lil.sh</h1>
      <h5>your free link shortener</h5>
      <div className="app-body">
        <RequestLink />
      </div>
    </div>

  );
};

export default HomePage;
