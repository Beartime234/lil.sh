import React, { Suspense, lazy } from 'react';
import { Switch, Route } from 'react-router-dom';
import {BarLoader} from "react-spinners";

const HomePage = lazy(() => import('../pages/HomePage'));
const InfoPage = lazy(() => import('../pages/InfoPage'));
const ErrorPage = lazy(() => import('../pages/ErrorPage'));


const Routes = () => {
  return (
    <Suspense fallback={<div style={{ position: "fixed", top: "55%", left: "50%", transform: "translate(-50%, -50%)" }}>
      <BarLoader
        size={150}
        color={"#616161"}
        loading={true}
      />
    </div>}>
      <Switch>
        <Route exact path="/" component={HomePage} />
        <Route exact path="/info" component={InfoPage} />
        <Route component={_ => <ErrorPage status={404} message="Link not found." />} />
      </Switch>
    </Suspense>
  );
};

export default Routes;
