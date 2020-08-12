import React from 'react';
/** @jsx jsx */
import { jsx, css } from '@emotion/core';
import RequestLink from "../components/RequestLink";

const HomePageStyle = css`
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
`;

const HomePage = () => {
  return (
    <div css={[HomePageStyle]}>
      <h1 className="title">lil.sh</h1>
      <h5>your free link shortener</h5>
      <div className="app-body">
        <RequestLink />
      </div>
    </div>

  );
};

export default HomePage;
