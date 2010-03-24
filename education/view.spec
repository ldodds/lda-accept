require File.join(File.dirname(__FILE__), "..", "helper/spec_helper.rb")

#Include shared_examples for JSON tests
require File.join( File.dirname(__FILE__), "..", "common/json_shared.rb")

#Include shared_examples for Education tests
require "edu_shared.rb"

describe "The Education API," do

  context "when accessing an unknown view" do
    
    before :all do
    ENV['server'] ||= 'localhost'
    @response = server_get "/doc/schools.json?_view=fubar"
    end

    it "should report a 400 Error" do
     @response.code.should == 400       
    end
  
  end
      
  context "requesting the short view" do
    before :all do
        ENV['server'] ||= 'localhost'
        @response = server_get "/doc/schools.json?_view=short"
    end
    
    it_should_behave_like "All JSON Requests"
    it_should_behave_like "All JSON List Endpoints"      
    it_should_behave_like "All School Requests"
    
    it "should return only the expected properties" do
      query(@response, "$.result.items").each do |school|
        rejects = school.keys.reject do |item|
          ["type", "label", "establishmentStatus", "typeOfEstablishment"].include?(item)
        end
        rejects.size.should == 0
      end
    end
  end
  
  context "requesting the medium view" do
    before :all do
        ENV['server'] ||= 'localhost'
        @response = server_get "/doc/schools.json?_view=medium"
    end
    
    it_should_behave_like "All JSON Requests"
    it_should_behave_like "All JSON List Endpoints"      
    it_should_behave_like "All School Requests"
    
    it "should return only the expected properties" do
      query(@response, "$.result.items").each do |school|
        rejects = school.keys.reject do |item|
          ["type", "label", "establishmentStatus", "typeOfEstablishment", "schoolCapacity", "phaseOfEducation", 
          "districtAdministrative", "parliamentaryConstituency", "administrativeWard", "nurseryProvision"].include?(item)
        end
        rejects.size.should == 0
      end
    end
  end  
  
  context "requesting the geo view" do
    before :all do
        ENV['server'] ||= 'localhost'
        @response = server_get "/doc/schools.json?_view=geo"
    end
    
    it_should_behave_like "All JSON Requests"
    it_should_behave_like "All JSON List Endpoints"      
    it_should_behave_like "All School Requests"
    
    it "should return only the expected properties" do
      query(@response, "$.result.items").each do |school|
        rejects = school.keys.reject do |item|
          ["type", "label", "establishmentStatus", "lat", "long"].include?(item)
        end
        rejects.size.should == 0
      end
    end
  end
    
end