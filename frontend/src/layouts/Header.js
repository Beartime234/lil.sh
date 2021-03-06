import React from 'react';
import { Link, useLocation } from 'react-router-dom';
/** @jsx jsx */
import { jsx, css } from '@emotion/core';

import { ReactComponent as SunIcon } from '../assets/sun.svg';
import { ReactComponent as MoonIcon } from '../assets/moon.svg';
import { ReactComponent as ShIconWhite } from '../assets/sh_white.svg';
import { ReactComponent as ShIconBlack } from '../assets/sh_black.svg';
import media from '../styles/media';
import { palette } from '../styles/palette';
import { useThemeContext } from '../contexts/ThemeContext';

const headerStyle = (isLight) => css`
  height: 60px;
  ${media.medium} {
    height: 50px;
  }

  & > nav {
    height: 100%;
    display: flex;
    padding: 0 12px;
    margin: 0 auto;
    max-width: 1440px;
    align-items: center;
    justify-content: space-between;

    .logo a {
      height: 100%;
      display: flex;
      align-items: center;
      font-size: 2rem;
      font-weight: bold;
      text-decoration: none;
      text-transform: lowercase;

      svg {
        width: 2rem;
        height: 2rem;
        margin-right: 0.5rem;
      }
    }

    svg {
      color: ${isLight ? 'inherit' : palette.yellow[4]};
      fill: ${isLight ? palette.yellow[6] : palette.yellow[4]};
    }

    svg.theme {
      cursor: pointer;
      display: flex;
      user-select: none;
    }
  }
`;

const Header = () => {
  const { pathname } = useLocation();
  const { isLight, toggleTheme } = useThemeContext();

  return (
    <header css={[headerStyle(isLight)]}>
      <nav>
        <div className="logo">
          <Link to="/" replace={pathname === '/'}>
            {isLight ? (
                <ShIconBlack />
            ) : (
                <ShIconWhite />
            )}
            lil.sh
          </Link>
        </div>
        <div>
          {isLight ? (
            <SunIcon className="theme" onClick={toggleTheme} />
          ) : (
            <MoonIcon className="theme" onClick={toggleTheme} />
          )}
        </div>
      </nav>
    </header>
  );
};

export default Header;
