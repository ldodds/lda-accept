#
# Shared tests for responses that return schools
# 
shared_examples_for "All School Requests" do

  it "should return only schools" do
    non_schools = 0
    query(@response, "$.result.items").each do |school|
      has_school_type = false
      school["type"].each do |type|
        has_school_type = true if type["_about"] == "http://education.data.gov.uk/def/school/School"
      end
      non_schools = non_schools + 1 unless has_school_type
    end
    non_schools.should == 0
  end
    
  it "should have default page size" do
    query(@response, "$.result.items").size.should == 10
    query(@response, "$.result.itemsPerPage").should == 10     
  end
    
end
