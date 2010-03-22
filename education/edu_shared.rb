#
# Shared tests for responses that return schools
# 
shared_examples_for "All School Requests" do

  it "should return only schools" do
    schools = 0    
    query(@response, "$.result.items").each do |school|
      school["type"].each do |type|
        schools = schools + 1 if type["_about"] == "http://education.data.gov.uk/def/school/School"
      end
    end
    schools.should == 10
  end

  it "should have default page size" do
    query(@response, "$.result.items").size.should == 10  
  end
    
end
