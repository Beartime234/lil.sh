import React from 'react';
import { Link } from 'react-router-dom';
/** @jsx jsx */
import { jsx, css } from '@emotion/core';
import { default as TakenSVG } from '../assets/undraw_Taken.svg';
import { palette } from '../styles/palette';
import { useThemeContext } from '../contexts/ThemeContext';
import media from '../styles/media';

const ErrorPageStyle = (isLight) => css`
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;

  h1 {
    font-size: 3rem;
    font-weight: 600;
  }
  img {
    margin: 1rem auto;
    max-width: 35%;
  }
  a {
    color: ${isLight ? palette.blue[6] : palette.blue[4]};
  }
  
  li {
    line-height: 1.5;
  }

  ${media.medium} {
    img {
      margin: 2rem auto;
      max-width: 70%;
    }
  }
  ${media.small} {
    h1 {
      font-size: 2.5rem;
    }
    img {
      margin: 2rem auto;
      max-width: 80%;
    }
  }
`;

const ErrorPage = () => {
  const { isLight } = useThemeContext();

  return (
    <div css={[ErrorPageStyle(isLight)]}>
      <h1>Information</h1>
      <ul>
        <li>Links last 31 days from creation and then are deleted.</li>
        <li>You can use them anywhere.</li>
        <li>You can use them to link to anything.</li>
        <li>Be responsible. The site owner may terminate links if used irresponsibly.</li>
        <li>No content that lil.sh links to is owned by the site owner.</li>
      </ul>
      <br/>
      <Link to="/">Make a link</Link>
    </div>
  );
};

export default ErrorPage;
