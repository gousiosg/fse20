﻿/*
Copyright 2013 George Edwards

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License. 
*/
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using DomainPro.Analyst.Types;
using DomainPro.Analyst.Engine;

namespace DomainPro.Analyst.Interfaces
{
    public interface DP_IObject
    {
        void Initialize();
        DP_IObject Create(string typeName);

        Guid Id
        { get; set; }
        DP_ConcreteType Type
        { get; set; }
        DP_IObject Context
        { get; set; }
        DP_IModel Model
        { get; set; }
        DP_Random Random
        { get; }
        double Time
        { get; }
        //Dictionary<Guid, DP_IObject> Objects
        //{ get; set; }
        Dictionary<Guid, DP_ILink> Links
        { get; set; }
        Dictionary<Guid, DP_IDependency> Dependencies
        { get; set; }
    }
}
