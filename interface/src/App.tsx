import { useState } from 'react'

import './App.css'
import { BrowserRouter, Route, Routes } from 'react-router-dom'
import PAGES from './views/pages'
import Login from './views/login/login'
import Operator from './views/operator/operator'
import Offical from './views/official/official'

function App() {

  return (
    <BrowserRouter>
      <Routes>
        <Route path={PAGES.LOGIN} element={<Login />} />
        <Route path={PAGES.OPERATOR} element={<Operator />} />
        <Route path={PAGES.OFFICIAL} element={<Offical />} />
      </Routes>
    
    </BrowserRouter>
  )
}

export default App
