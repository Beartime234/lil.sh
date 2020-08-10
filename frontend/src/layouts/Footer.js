import React from 'react';
/** @jsx jsx */
import { jsx, css } from '@emotion/core';
import { ReactComponent as GithubIcon } from '../assets/github.svg';

const footerStyle = css`
  padding: 40px 16px;
  & > nav {
    margin: 0 auto;
    max-width: 1440px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    
    .love {
      color: red
    }
    
    svg {
      width: 2rem;
      height: 2rem;
    }
  }
`;

const Footer = () => {
  return (
    <footer css={[footerStyle]}>
      <nav>
        <div><a href="https://josheaton.co.nz">Josh Eaton</a> made with <span className="love">❤</span></div>
        <div>
          <a
            href="https://github.com/Beartime234/lil.sh"
            rel="noopener noreferrer"
            target="_blank"
          >
            <GithubIcon className="github" />
          </a>
        </div>
      </nav>
    </footer>
  );
};

export default Footer;
