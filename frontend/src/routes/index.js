import React, { Suspense, lazy } from 'react';
import { Switch, Route, Redirect } from 'react-router-dom';
import {BarLoader} from "react-spinners";
import {useThemeContext} from "../contexts/ThemeContext";


const HomePage = lazy(() => import('../pages/HomePage'));
const InfoPage = lazy(() => import('../pages/InfoPage'));
const ErrorPage = lazy(() => import('../pages/ErrorPage'));



const Routes = () => {
  const { isLight } = useThemeContext();

  return (
    <Suspense fallback={<div style={{ position: "fixed", top: "55%", left: "50%", transform: "translate(-50%, -50%)" }}>
      <BarLoader
        size={150}
        color={ isLight ? "#616151" : "red" }
        loading={true}
      />
    </div>}>
      <Switch>
        <Route exact path="/" component={HomePage} />
        <Route exact path="/info" component={InfoPage} />
        <Route exact path="/surl/base.redirect">
          <Redirect to="/" />
        </Route>
        <Route component={_ => <ErrorPage status={404} message="Link not found." />} />
      </Switch>
    </Suspense>
  );
};

export default Routes;
